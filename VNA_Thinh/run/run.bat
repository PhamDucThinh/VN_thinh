set logdir="C:\myproject\VNA_Thinh\reports\" %date:~-4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
mkdir %logdir%

:: run the automation script
call python -m robot.run --outputdir %logdir% --variablefile C:\myproject\VNA_Thinh\MEAU_test_variable.py --suite * C:\My_project\VNA_Thinh\VNA_booking.robot
pause...