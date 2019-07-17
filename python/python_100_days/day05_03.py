"""
“百钱百鸡”问题
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

Version: 0.1
Author: ndsunl
"""

print("百钱百鸡：")
for hens in range(101):
    for cocks in range(101):
        if 8 * hens + 14 * cocks == 200:
            print(f"公鸡 {cocks} 只、母鸡 {hens} 只、小鸡 {100 - cocks - hens}")