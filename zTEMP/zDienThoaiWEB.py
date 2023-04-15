import subprocess

# LINK
LINK = "http://127.0.0.1:5500/DoAn1/testFE/index.html"
# LINK


output = subprocess.check_output(["ipconfig"]).decode("utf-8")
ipv4_line = [line.strip() for line in output.split("\n") if "IPv4 Address" in line][0]
ipv4_address = ipv4_line.split(":")[-1].strip()
print(f"""
______________________________________________________________________

{LINK.replace("127.0.0.1",ipv4_address)}
______________________________________________________________________
""")