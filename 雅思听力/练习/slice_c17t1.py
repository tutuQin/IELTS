#!/usr/bin/env python3
"""
剑桥雅思 17 Test 1 Part 1 错题与考点音频高精度切片脚本
对齐官方听力文本: c17t1_official_tapescript.txt
母带音频: full_test1.mp3
"""

import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(BASE_DIR, "C17T1_错题音频切片")
FULL_SOURCE = os.path.join(TARGET_DIR, "full_test1.mp3")

# 1. Part 1 完整模考录音 (包含题目介绍、审题、两段对话及检查时间，共 5分32秒)
SECTION_1_START = 46.5
SECTION_1_END = 378.5

# 2. Q1 - Q10 靶向考点精切区间 (基于 full_test1.mp3 精确对齐)
SLICES = [
    (
        "01_Q1_海滩无垃圾litter与free_of否定改写.mp3",
        115.0,
        134.0,
        "Q1 · 海滩无垃圾清理 (litter) [115.0s ~ 134.0s]"
    ),
    (
        "02_Q2_海滩禁狗dogs与悬崖散步cliff干扰.mp3",
        133.0,
        147.5,
        "Q2 · 海滩禁狗规则与悬崖干扰 (dogs) [133.0s ~ 147.5s]"
    ),
    (
        "03_Q3_吸引昆虫insects与人工巢箱铺垫.mp3",
        164.5,
        181.0,
        "Q3 · 保护区吸引昆虫 (insects) [164.5s ~ 181.0s]"
    ),
    (
        "04_Q4_识别蝴蝶物种butterflies与复数形态.mp3",
        180.5,
        198.5,
        "Q4 · 识别蝴蝶物种与复数形态 (butterflies) [180.5s ~ 198.5s]"
    ),
    (
        "05_Q5_重砌新墙wall与暴风雨破坏storm干扰.mp3",
        198.0,
        211.5,
        "Q5 · 重砌新墙与暴风雨破坏干扰 (wall) [198.0s ~ 211.5s]"
    ),
    (
        "06_Q6_徒步海岛island与沙滩退潮定位.mp3",
        257.5,
        282.5,
        "Q6 · 徒步海岛与退潮沙滩 (island) [257.5s ~ 282.5s]"
    ),
    (
        "07_Q7_涉水防水靴boots与野餐picnic排除.mp3",
        294.0,
        317.0,
        "Q7 · 涉水防水靴与野餐排除 (boots) [294.0s ~ 317.0s]"
    ),
    (
        "08_Q8_木工初学者beginners与提问先出答案倒装.mp3",
        316.5,
        336.5,
        "Q8 · 木工初学者与跨角色提问倒装 (beginners) [316.5s ~ 336.5s]"
    ),
    (
        "09_Q9_制作木勺spoons与做椅子chairs干扰.mp3",
        336.5,
        352.5,
        "Q9 · 制作木勺与做椅子干扰 (spoons) [336.5s ~ 352.5s]"
    ),
    (
        "10_Q10_基本费用35镑与露营40镑条件排除.mp3",
        352.5,
        374.0,
        "Q10 · 基本费用与露营附加费排除 (35) [352.5s ~ 374.0s]"
    ),
]


def cut_audio():
    print(f"=== 开始切片 剑桥雅思 17 Test 1 Part 1 ===")
    print(f"源文件: {FULL_SOURCE}")

    # 1. 切完整 Part 1
    full_out = os.path.join(TARGET_DIR, "Section_1_Full_Buckworth_Conservation_Group.mp3")
    print(f"\n[1/11] 导出完整 Part 1 录音 -> {os.path.basename(full_out)}")
    cmd_full = [
        "ffmpeg", "-y",
        "-ss", str(SECTION_1_START),
        "-to", str(SECTION_1_END),
        "-i", FULL_SOURCE,
        "-c:a", "libmp3lame",
        "-q:a", "2",
        full_out
    ]
    subprocess.run(cmd_full, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 2. 切 10 个考点音频
    for idx, (filename, start, end, desc) in enumerate(SLICES, start=2):
        out_path = os.path.join(TARGET_DIR, filename)
        dur = end - start
        print(f"[{idx}/11] 切片: {desc} (时长: {dur:.1f}s)")
        cmd = [
            "ffmpeg", "-y",
            "-ss", str(start),
            "-t", str(dur),
            "-i", FULL_SOURCE,
            "-c:a", "libmp3lame",
            "-q:a", "2",
            out_path
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("\n✅ 所有音频切片与完整录音导出完成！")


if __name__ == "__main__":
    cut_audio()

