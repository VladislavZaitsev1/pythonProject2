import wmi

w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
# print(temperature_infos)
for sensor in temperature_infos:
    # print(sensor)
    if sensor.SensorType == 'Temperature':
        print(sensor.Name)
        print(sensor.Value)