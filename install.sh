sudo apt update
sudo apt upgrade -y
sudo apt install -y python3-pip python3-dev

sudo apt install python3-venv  # 가상 환경 모듈 설치 (필요 시)
python3 -m venv myenv          # 가상 환경 생성
source myenv/bin/activate      # 가상 환경 활성화
pip install locust             # 가상 환경 내에 Locust 설치
