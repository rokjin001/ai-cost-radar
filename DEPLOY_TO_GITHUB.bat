@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
set /p REPO_URL=GitHub 저장소 URL을 붙여넣으세요 (예: https://github.com/아이디/ai-cost-radar.git): 
if "%REPO_URL%"=="" (
    echo [취소] URL이 입력되지 않았습니다.
    pause
    exit /b 1
)
git remote remove origin >nul 2>&1
git remote add origin "%REPO_URL%"
git push -u origin main
if errorlevel 1 (
    echo [오류] 푸시에 실패했습니다. GitHub 로그인 창이 뜨면 승인해 주세요.
    pause
    exit /b 1
)
echo [완료] GitHub 푸시 성공! 저장소 Settings -> Pages -> Source를 'GitHub Actions'로 선택하면 1분 뒤 전 세계에 공개됩니다.
pause
endlocal
