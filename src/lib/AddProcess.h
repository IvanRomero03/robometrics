#include <fcntl.h>
#include <unistd.h>

#define PIPEFILE "/tmp/worker"

namespace AddProcess
{
    int AddProcessByPID(int pid)
    {
        char *pipefile = PIPEFILE;
        int handle = open(pipefile, O_WRONLY);
        if (handle == -1)
        {
            return -1;
        }
        write(handle, &pid, sizeof(pid));
        close(handle);
        return 0;
    }

    int UnregisterProcessByPID(int pid)
    {
        char *pipefile = PIPEFILE;
        pid *= -1;
        int handle = open(pipefile, O_WRONLY);
        if (handle == -1)
        {
            return -1;
        }
        write(handle, &pid, sizeof(pid));
        close(handle);
        return 0;
    }

    int AutoRegisterProcess()
    {
        char *pipefile = PIPEFILE;
        int handle = open(pipefile, O_WRONLY);
        if (handle == -1)
        {
            return -1;
        }
        int pid = getpid();
        write(handle, &pid, sizeof(pid));
        close(handle);
        return 0;
    }

    int AutoUnregisterProcess()
    {
        char *pipefile = PIPEFILE;
        int handle = open(pipefile, O_WRONLY);
        if (handle == -1)
        {
            return -1;
        }
        int pid = getpid();
        pid *= -1;
        write(handle, &pid, sizeof(pid));
        close(handle);
        return 0;
    }
}