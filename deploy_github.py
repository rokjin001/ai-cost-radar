"""Safe GitHub push helper (handles Korean/space paths and UTF-8 prompts cleanly)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> int:
    print("============================================================")
    print("  AI Cost Radar -> GitHub Pages 자동 배포")
    print("============================================================")
    repo_url = input("GitHub 저장소 URL을 붙여넣으세요 (예: https://github.com/아이디/ai-cost-radar.git): ").strip().strip('"').strip("'")
    if not repo_url:
        print("[취소] URL이 입력되지 않았습니다.")
        return 1

    subprocess.run(["git", "remote", "remove", "origin"], cwd=str(ROOT), capture_output=True)
    r1 = subprocess.run(["git", "remote", "add", "origin", repo_url], cwd=str(ROOT))
    if r1.returncode != 0:
        print("[오류] 원격 저장소 등록에 실패했습니다.")
        return r1.returncode

    print("[진행] GitHub로 푸시 중... (로그인 창이 뜨면 브라우저에서 승인해 주세요)")
    r2 = subprocess.run(["git", "push", "-u", "origin", "main"], cwd=str(ROOT))
    if r2.returncode != 0:
        print("[오류] 푸시에 실패했습니다. 저장소가 비어 있는지(README 미생성)와 로그인 상태를 확인해 주세요.")
        return r2.returncode

    print("\n[완료] GitHub 푸시 성공!")
    print("다음 단계: GitHub 저장소 -> Settings -> Pages -> Source를 'GitHub Actions'로 선택하세요.")
    return 0


if __name__ == "__main__":
    code = main()
    input("\n엔터(Enter)를 누르면 창이 닫힙니다...")
    raise SystemExit(code)
