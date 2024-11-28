import asyncio

async def run_command(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()
    print(f'{cmd} zakończono z {proc.returncode}')
    if stdout:
        print(f' {stdout}\n{stdout.decode()}')
    if stderr:
        print(f' {stderr}\n{stderr.decode()}')

async def main():
    command = 'cd .'
    await run_command(command)

asyncio.run(main())
