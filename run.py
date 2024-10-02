from app import create_app


if __name__ == '__main__':
    # 创建app对象
    app = create_app()
    # 启动app
    app.run(debug=True)

