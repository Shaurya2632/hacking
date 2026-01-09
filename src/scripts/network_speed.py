import speedtest

speed = speedtest.Speedtest()

uploadSpeed = speed.upload() / 1_000_000
downloadSpeed = speed.download() / 1_000_000

print(f"Upload Speed: {uploadSpeed:.2f} Mbps")
print(f"Download Speed: {downloadSpeed:.2f} Mbps")