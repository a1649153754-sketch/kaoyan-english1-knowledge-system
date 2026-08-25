$ErrorActionPreference = "Stop"
$Repo = "a1649153754-sketch/kaoyan-english1-knowledge-system"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw "请先安装 Git。" }
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw "请先安装 GitHub CLI。" }
gh auth status 2>$null
if ($LASTEXITCODE -ne 0) { gh auth login }
if (-not (Test-Path .git)) { git init }
git add -A
git commit -m "feat: initialize kaoyan English I knowledge system v1.0.0" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "没有新的本地改动，继续检查远端。" }
git branch -M main
$remote = (git remote get-url origin 2>$null)
if (-not $remote) { git remote add origin "https://github.com/$Repo.git" }
else { git remote set-url origin "https://github.com/$Repo.git" }
git push -u origin main
Write-Host "上传完成：https://github.com/$Repo" -ForegroundColor Green
Write-Host "Pages 设置完成后，站点为：https://a1649153754-sketch.github.io/kaoyan-english1-knowledge-system/"
