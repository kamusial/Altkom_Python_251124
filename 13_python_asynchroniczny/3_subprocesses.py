import asyncio
import locale

async def run_command(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    encoding = locale.getpreferredencoding()
    stdout, stderr = await proc.communicate()

    if stdout:
        print(f' {stdout}\n{stdout.decode(encoding)}')
    if stderr:
        print(f' {stderr}\n{stdout.decode(encoding)}')

async def main():
    command = 'dir'
    await run_command(command)

asyncio.run(main())
