import os
from flask import Flask

def create_app(test_config=None):
    # 앱 생성 및 설정 
    app= Flask(__name__,instance_relative_config=True) 
    app.config.from_mapping(SECRECT_KEY='dev',
                            DATABASE=os.path.join(app.instance_path,'')
                            )
    