#!groovy
pipeline {
    //在任何可用的代理上执行Pipeline
    agent {
      label '192.168.20.77'
    }
    //参数化变量，目前只支持[booleanParam, choice, credentials, file, text, password, run, string]这几种参数类型，其他高级参数化类型还需等待社区支持。
    parameters {
        //服务器参数采用了组合方式，避免多次选择，使用docker为更佳实践【参数值对外隐藏】
        choice (choices: ['192.168.19.76', '192.168.19.90'], description: '请选择TSE服务器', name: 'TSE')
        choice (choices: ['192.168.19.77', '192.168.19.91'], description: '请选择TSI服务器', name: 'TSI')
        //测试服务器的dubbo服务端口
    }
    //pipeline的各个阶段场景
    stages {
        stage('Params_Prepare') {
            steps {
                //根据param.server分割获取参数,包括IP,jettyPort,username,password
                script {
                    def s1 = params.TSE.split("\\.")
                    tse_ip=s1[3]
                    def s2=params.TSI.split("\\.")
                    tsi_ip=s2[3]
                    TOPOS_E="DTS-TOPOS-${tse_ip}"
                    TOPOS_I="DTS-TOPOS-${tsi_ip}"
                }
                echo "我的参数TSE:   ${params.TSE}"
                echo "我的参数tse_ip:   ${tse_ip}"
                echo "我的参数tsi_ip:   ${tsi_ip}"
                echo "我的参数TOPOS_E:   ${TOPOS_E}"
                echo "我的参数TOPOS_I:   ${TOPOS_I}"
                
                sh'''for((i=1;i<=20;i++)); do  if ping -c 1 -W 3 $TSE >/dev/null; then  echo "$TSE Ping is success";    break; fi; done ; sleep 60
                for((i=1;i<=20;i++)); do  if ping -c 1 -W 3 $TSI >/dev/null; then  echo "$TSE Ping is success";    break; fi; done ; sleep 60'''
            }
        }
        stage('INIT_OS') {
            steps {
                script {
                    if ("${TSE}" == "192.168.19.76"){
                        sshPublisher(publishers: [sshPublisherDesc(configName: '192.168.16.123', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '''virsh snapshot-revert DTS-TOPOS-76 DTS-TOPOS-76
                            #开机
                            virsh start DTS-TOPOS-76
                            
                            virsh snapshot-revert DTS-TOPOS-77 DTS-TOPOS-77
                            #开机
                            virsh start DTS-TOPOS-77
                            sleep 180''', execTimeout: 360000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
                    }
                    if ("${TSE}" == "192.168.19.90"){
                        sshPublisher(publishers: [sshPublisherDesc(configName: '192.168.16.123', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '''virsh snapshot-revert DTS-TOPOS-90 DTS-TOPOS-90
                            #开机
                            virsh start DTS-TOPOS-90
                            
                            virsh snapshot-revert DTS-TOPOS-91 DTS-TOPOS-91
                            #开机
                            virsh start DTS-TOPOS-91
                            sleep 180''', execTimeout: 360000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                sh "rm -rf $WORKSPACE/*"
                sh "cp /home/package/Topwalk-DTS/DTS2.1/dtsInstall/packages/script/* $WORKSPACE/"
            
                sshPublisher(publishers: [sshPublisherDesc(configName: "${TSE}", transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '''source /etc/profile
                    ln -s /usr/local/bin/uudecode /usr/bin/uudecode
                    cd /root
                    chmod u+x *
                    sh ceshi.sh 1
                    sleep 180
                    sed -ri "s/^IPADDR=.*/IPADDR=$TSE/" /etc/sysconfig/network-scripts/ifcfg-eth0
                    sh Change_IP90.sh''', execTimeout: 800000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '/root', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '*')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
            
                sshPublisher(publishers: [sshPublisherDesc(configName: "${TSI}", transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: '''source /etc/profile
                    ln -s /usr/local/bin/uudecode /usr/bin/uudecode
                    cd /root
                    chmod u+x *
                    sh ceshi.sh 2
                    sleep 180
                    sed -ri "s/^IPADDR=.*/IPADDR=$TSI/" /etc/sysconfig/network-scripts/ifcfg-eth0
                    sh Change_IP90.sh''', execTimeout: 800000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '/root', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '*')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
            
                buildDescription '部署环境:TSE:${TSE} && TSI:${TSI}'
            }
        }
    }
}