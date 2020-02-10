# コンパイル
colcon build;

# コンパイルの出力先フォルダにパスを通す
# source install/setup.bash && source install/local_setup.bash;


# talkerの実行
ros2 run ros2_py_pkg my_talker;

# listenerの実行
# ros2 run my_python my_listener
