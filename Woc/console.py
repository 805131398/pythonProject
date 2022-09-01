from wisepaasdatahubedgesdk.EdgeAgent import EdgeAgent
import wisepaasdatahubedgesdk.Common.Constants as constant
from wisepaasdatahubedgesdk.Model.Edge import EdgeAgentOptions, MQTTOptions, DCCSOptions, EdgeData, EdgeTag, EdgeStatus, \
    EdgeDeviceStatus, EdgeConfig, NodeConfig, DeviceConfig, AnalogTagConfig, DiscreteTagConfig, TextTagConfig
from wisepaasdatahubedgesdk.Common.Utils import RepeatedTimer


class YanHua:

    def on_connected(self, edgeAgent, isConnected):
        print("connected !")
        config = self.generateConfig()
        self._edgeAgent.uploadConfig(action=constant.ActionType['Create'], edgeConfig=config)

    @staticmethod
    def on_disconnected(edgeAgent, isDisconnected):
        print("disconnected !")

    @staticmethod
    def edgeAgent_on_message(agent, messageReceivedEventArgs):
        print("edgeAgent_on_message !")

    def sendData(self, deviceInfo):
        for key, value in deviceInfo.items():
            data = self.generateData(key=key, value=value, deviceInfo=deviceInfo)
            self._edgeAgent.sendData(data)

    def generateData(self, key, value, deviceInfo):
        edgeData = EdgeData()
        deviceId = deviceInfo['projectName']
        tag = EdgeTag(deviceId, f'{deviceInfo["ab_name"]}_{key}', value)
        edgeData.tagList.append(tag)
        return edgeData

    def generateConfig(self):
        config = EdgeConfig()

        deviceConfig = DeviceConfig(id=self.deviceInfo['projectName'],
                                    name=self.deviceInfo['projectName'],
                                    description=self.deviceInfo['description'],
                                    deviceType=self.deviceInfo['deviceType'],
                                    retentionPolicyName=self.deviceInfo['retentionPolicyName'])

        sh265_up_bytes_insight = TextTagConfig(name=f'{self.deviceInfo["ab_name"]}_up_bytes_insight',
                                               description=f'{self.deviceInfo["projectName"]}上行瞬时流量[单位(Kbps)]',
                                               readOnly=True,
                                               arraySize=0)
        deviceConfig.textTagList.append(sh265_up_bytes_insight)

        sh265_down_bytes_insight = TextTagConfig(name=f'{self.deviceInfo["ab_name"]}_down_bytes_insight',
                                                 description=f'{self.deviceInfo["projectName"]}下行瞬时流量[单位(Kbps)]',
                                                 readOnly=True,
                                                 arraySize=0)
        deviceConfig.analogTagList.append(sh265_down_bytes_insight)

        sh265_cumulative = TextTagConfig(name=f'{self.deviceInfo["ab_name"]}_cumulative',
                                         description=f'{self.deviceInfo["projectName"]}累计流量',
                                         readOnly=True,
                                         arraySize=0)
        deviceConfig.analogTagList.append(sh265_cumulative)

        sh265_cumulative = TextTagConfig(name=f'{self.deviceInfo["ab_name"]}_cumulative',
                                         description=f'{self.deviceInfo["projectName"]}累计流量',
                                         readOnly=True,
                                         arraySize=0)
        deviceConfig.analogTagList.append(sh265_cumulative)

        sh265_ip = TextTagConfig(name=f'{self.deviceInfo["ab_name"]}_ip',
                                 description=f'{self.deviceInfo["projectName"]}使用的 ip 地址',
                                 readOnly=True,
                                 arraySize=0)
        deviceConfig.analogTagList.append(sh265_ip)

        sh265_networkStatus = TextTagConfig(name=f'{self.deviceInfo["ab_name"]}_networkStatus',
                                            description=f'{self.deviceInfo["projectName"]}使用的网络状态',
                                            readOnly=True,
                                            arraySize=0)
        deviceConfig.analogTagList.append(sh265_networkStatus)

        config.node.deviceList.append(deviceConfig)
        return config

    def __init__(self, deviceInfo):
        self.deviceInfo = deviceInfo

        print("deviceConfig = :", self.deviceInfo['projectName'],
              self.deviceInfo['projectName'],
              self.deviceInfo['description'],
              self.deviceInfo['deviceType'],
              self.deviceInfo['retentionPolicyName'])

        self._edgeAgent = None
        edgeAgentOptions = EdgeAgentOptions(nodeId='b3fc00c1-2e38-464d-89dc-25712b13f1be')
        edgeAgentOptions.connectType = constant.ConnectType['DCCS']
        dccsOptions = DCCSOptions(apiUrl='http://api-dccs-ensaas.yy.sdgs.com.cn/',
                                  credentialKey='553fc85b511d4ee04e4d76efb25c12o8')
        edgeAgentOptions.DCCS = dccsOptions
        self._edgeAgent = EdgeAgent(edgeAgentOptions)
        self._edgeAgent.on_connected = self.on_connected
        self._edgeAgent.on_disconnected = self.on_disconnected
        self._edgeAgent.on_message = self.edgeAgent_on_message
        self._edgeAgent.connect()
        print("研华 SDK初始化完成")
