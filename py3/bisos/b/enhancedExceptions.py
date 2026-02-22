# -*- coding: utf-8 -*-

""" #+begin_org
* Enhanced Exception Formatting for BISOS CSXUs

Provides detailed exception tracebacks with local variable context.
Install by importing: from bisos.b import enhancedExceptions

This module installs a custom exception hook as a side effect of import.
Just importing this module enables enhanced exception formatting for the
entire Python process.

** Usage
#+begin_src python
from bisos.b import enhancedExceptions  # Enable enhanced exceptions

# Rest of CSXU code...
#+end_src

** Optional Control
After importing, you can control the formatting:
#+begin_src python
enhancedExceptions.disable()  # Disable if needed
enhancedExceptions.enable()   # Re-enable
if enhancedExceptions.is_enabled():
    print("Enhanced exceptions are active")
#+end_src

#+end_org """

import sys
import traceback

# Optional: Import better_exceptions if available
try:
    import better_exceptions
    _BETTER_EXCEPTIONS_AVAILABLE = True
except ImportError:
    _BETTER_EXCEPTIONS_AVAILABLE = False
    better_exceptions = None


####+BEGIN: bx:cs:py3:section :title "ContextualExceptionFormatter Class"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *ContextualExceptionFormatter Class*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

class ContextualExceptionFormatter:
    """Enhanced exception formatter that automatically extracts function arguments"""
    
    def __init__(self, max_var_length=150, max_other_vars=5, max_frames=10):
        """
        Initialize the formatter.
        
        Args:
            max_var_length: Maximum length of variable representation
            max_other_vars: Max number of non-argument variables to show
            max_frames: Maximum number of stack frames to display
        """
        self.max_var_length = max_var_length
        self.max_other_vars = max_other_vars
        self.max_frames = max_frames
    
    @staticmethod
    def _should_show_var(var_name):
        """Determine if variable should be displayed"""
        # Skip private/magic variables
        if var_name.startswith('_'):
            return False
        # Skip double underscore names
        if '__' in var_name:
            return False
        return True
    
    def _format_value(self, value):
        """Format a variable value for display"""
        try:
            var_repr = repr(value)
            if len(var_repr) > self.max_var_length:
                var_repr = var_repr[:self.max_var_length] + "..."
            return var_repr
        except Exception as e:
            return f"<repr() failed: {type(e).__name__}>"
    
    @staticmethod
    def _get_function_arguments(frame):
        """
        Extract function argument names and their values from a frame.
        
        This inspects the code object to find all argument names
        (positional, keyword-only, *args, **kwargs) and returns
        their values from the frame's locals.
        
        Returns:
            tuple: (arguments_dict, argument_names_set)
        """
        code = frame.f_code
        locals_dict = frame.f_locals
        
        # Get positional argument names
        arg_count = code.co_argcount
        arg_names = code.co_varnames[:arg_count]
        
        # Get keyword-only argument names
        kwonly_count = code.co_kwonlyargcount
        kwonly_start = arg_count
        kwonly_names = code.co_varnames[kwonly_start:kwonly_start + kwonly_count]
        
        # Get *args name (if present)
        varargs_name = code.co_varnames[kwonly_start + kwonly_count] if code.co_flags & 0x04 else None
        
        # Get **kwargs name (if present)
        varkw_name = code.co_varnames[kwonly_start + kwonly_count + (1 if varargs_name else 0)] if code.co_flags & 0x08 else None
        
        # Combine all argument names
        all_arg_names = set(arg_names) | set(kwonly_names)
        if varargs_name:
            all_arg_names.add(varargs_name)
        if varkw_name:
            all_arg_names.add(varkw_name)
        
        # Get their values from frame locals
        arguments = {}
        for arg_name in all_arg_names:
            if arg_name in locals_dict:
                arguments[arg_name] = locals_dict[arg_name]
        
        return arguments, all_arg_names
    
    def _categorize_vars(self, frame):
        """Separate variables into arguments and other locals"""
        # Get function arguments
        arguments, arg_names = self._get_function_arguments(frame)
        
        # Get other local variables (not arguments)
        other_vars = {}
        for name, value in frame.f_locals.items():
            if not self._should_show_var(name):
                continue
            if name not in arg_names:
                other_vars[name] = value
        
        return arguments, other_vars
    
    def _get_function_call_signature(self, frame, arguments):
        """
        Build a function call signature like: module.function(arg1=value1, arg2=value2)
        
        Returns:
            str: Function call signature with argument values
        """
        code = frame.f_code
        func_name = code.co_name
        
        # Build argument string: arg1=value1, arg2=value2
        arg_strings = []
        for arg_name in sorted(arguments.keys()):
            arg_value = self._format_value(arguments[arg_name])
            arg_strings.append(f"{arg_name}={arg_value}")
        
        args_str = ", ".join(arg_strings)
        
        return f"{func_name}({args_str})"
    
    def format_exception(self, exc_type, exc_value, exc_traceback):
        """Format exception in standard Python traceback style with argument values"""
        lines = []
        # lines.append(f"\n{'='*80}")
        lines.append("Traceback (most recent call last):")
        
        tb = exc_traceback
        frame_num = 0
        
        while tb is not None and frame_num < self.max_frames:
            frame = tb.tb_frame
            frame_num += 1
            
            # Get function arguments
            arguments, other_vars = self._categorize_vars(frame)
            
            # Format like standard Python traceback
            filename = frame.f_code.co_filename
            lineno = tb.tb_lineno
            func_name = frame.f_code.co_name
            
            lines.append(f'  File "{filename}", line {lineno}, in {func_name}')
            
            # Build function call signature with argument values
            if arguments:
                func_call = self._get_function_call_signature(frame, arguments)
                lines.append(f"    {func_call}")
            
            # Optionally show other local variables (but less prominently)
            if other_vars and frame_num <= 2:
                for var_name in sorted(other_vars.keys())[:2]:  # Just show 2 other vars max
                    value_repr = self._format_value(other_vars[var_name])
                    lines.append(f"    # {var_name}={value_repr}")
            
            tb = tb.tb_next
        
        # Exception summary (standard Python format)
        lines.append(f"{exc_type.__name__}: {exc_value}")
        # lines.append(f"{'='*80}\n")
        
        return "\n".join(lines)


####+BEGIN: bx:cs:py3:section :title "Global State and Hooks"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Global State and Hooks*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# Global formatter instance
_formatter = ContextualExceptionFormatter()

# Track whether enhanced exceptions are enabled
_ENHANCED_EXCEPTIONS_ENABLED = False

# Store the original exception hook for restoration
_original_excepthook = sys.excepthook


def _enhanced_exception_hook(exc_type, exc_value, exc_traceback):
    """Custom exception hook - prints multiple perspectives of the exception"""
    # 1. Print standard Python traceback (for reference - comes first)
    print("="*80)
    print("STANDARD PYTHON TRACEBACK (for reference):")
    print("="*80)
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    
    # 2. Print better-exceptions output (with colors and local variables)
    if _BETTER_EXCEPTIONS_AVAILABLE and better_exceptions:
        print("\n" + "="*80)
        print("BETTER-EXCEPTIONS VIEW (with colors and local variables):")
        print("="*80)
        try:
            # better_exceptions.excepthook might not print, so call its core formatter
            # and print the output directly
            better_exceptions.excepthook(exc_type, exc_value, exc_traceback)
        except Exception as e:
            print(f"(better-exceptions processing failed: {e})")
    
    # 3. Print YOUR enhanced traceback (with argument values in function calls - comes last for visibility)
    print("\n" + "="*80)
    print("ENHANCED EXCEPTION TRACEBACK:")
    print("="*80)
    formatted = _formatter.format_exception(exc_type, exc_value, exc_traceback)
    print(formatted)


####+BEGIN: bx:cs:py3:section :title "Public Control Functions"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Public Control Functions*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

def is_enabled():
    """Check if enhanced exception formatting is currently enabled"""
    return _ENHANCED_EXCEPTIONS_ENABLED


def enable():
    """Enable enhanced exception formatting"""
    global _ENHANCED_EXCEPTIONS_ENABLED
    sys.excepthook = _enhanced_exception_hook
    _ENHANCED_EXCEPTIONS_ENABLED = True


def disable():
    """Disable enhanced exception formatting and restore original hook"""
    global _ENHANCED_EXCEPTIONS_ENABLED
    sys.excepthook = _original_excepthook
    _ENHANCED_EXCEPTIONS_ENABLED = False


def format_current_exception():
    """
    Format the current exception using enhanced formatting.
    
    Useful for catching and formatting exceptions that don't go through
    sys.excepthook (e.g., in atexit callbacks, threads, etc.)
    
    Returns:
        str: Formatted exception string
    """
    import sys as _sys
    exc_info = _sys.exc_info()
    if exc_info[0] is None:
        return "No current exception"
    
    exc_type, exc_value, exc_traceback = exc_info
    return _formatter.format_exception(exc_type, exc_value, exc_traceback)


####+BEGIN: bx:cs:py3:section :title "Module Initialization"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Module Initialization*  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# ============================================================================
# SIDE EFFECT: Install hook on import
# ============================================================================
# This is the key feature - just importing this module enables enhanced exceptions
# automatically. The module is only imported if explicitly requested by CSXUs.
enable()

####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
