def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            # Convert args in to something mutable
            newargs = []
            for (a, t) in zip(args, types):
                newargs.append( t(a))
            return f(*newargs, **kwargs)
        return new_func
    return decorator


# This is enforcing the types of the arguments, it also tries to convert the types if they aren't the 'str' and 'int'.
@enforce(str, int) 
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


repeat_msg("Kush", 5)


