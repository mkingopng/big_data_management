# install hadoop on ubuntu 22.04

#
sudo addgroup hadoop_

#
sudo adduser --ingroup hadoop_ hduser_

#
sudo adduser hduser_ sudo

#
Re-login as hduser_

# configure SSH
#
su - hduser_

#
ssh-keygen -t rsa -P ""

#
cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys

#
ssh localhost

#
sudo apt-get purge openssh-server

#
sudo apt-get install openssh-server

# download hadoop
sudo tar xzf hadoop-2.2.0.tar.gz

# 
sudo mv hadoop-2.2.0 hadoop

#
sudo chown -R hduser_:hadoop_ hadoop

#
# configure hadoop
# modify the ~/.bashrc file
# add the following lines to end of file ~/.bashrc

#Set HADOOP_HOME
export HADOOP_HOME=<Installation Directory of Hadoop>
#Set JAVA_HOME
export JAVA_HOME=<Installation Directory of Java>
# Add bin/ directory of Hadoop to PATH
export PATH=$PATH:$HADOOP_HOME/bin

#
. ~/.bashrc

#
sudo gedit $HADOOP_HOME/etc/hadoop/core-site.xml

#
<property>
<name>hadoop.tmp.dir</name>
<value>/app/hadoop/tmp</value>
<description>Parent directory for other temporary directories.</description>
</property>
<property>
<name>fs.defaultFS </name>
<value>hdfs://localhost:54310</value>
<description>The name of the default file system. </description>
</property>

#
sudo mkdir -p <Path of Directory used in above setting>

#
sudo chown -R hduser_:Hadoop_ <Path of Directory created in above step>

#
sudo chmod 750 <Path of Directory created in above step>

#
sudo gedit /etc/profile.d/hadoop.sh

#
export HADOOP_HOME=/home/guru99/Downloads/Hadoop

#
sudo chmod +x /etc/profile.d/hadoop.sh

#
sudo cp $HADOOP_HOME/etc/hadoop/mapred-site.xml.template $HADOOP_HOME/etc/hadoop/mapred-site.xml

#
sudo gedit $HADOOP_HOME/etc/hadoop/mapred-site.xml

#
<property>
<name>mapreduce.jobtracker.address</name>
<value>localhost:54311</value>
<description>MapReduce job tracker runs at this host and port.
</description>
</property>

#
sudo gedit $HADOOP_HOME/etc/hadoop/hdfs-site.xml

#
<property>
<name>dfs.replication</name>
<value>1</value>
<description>Default block replication.</description>
</property>
<property>
<name>dfs.datanode.data.dir</name>
<value>/home/hduser_/hdfs</value>
</property>

#
sudo mkdir -p <Path of Directory used in above setting>

#
sudo mkdir -p /home/hduser_/hdfs

#
sudo chown -R hduser_:hadoop_ <Path of Directory created in above step>

#
sudo chown -R hduser_:hadoop_ /home/hduser_/hdfs

#
sudo chmod 750 <Path of Directory created in above step>

#
sudo chmod 750 /home/hduser_/hdfs

#
$HADOOP_HOME/bin/hdfs namenode -format

#
$HADOOP_HOME/sbin/start-dfs.sh

#
$HADOOP_HOME/sbin/start-yarn.sh

#
$HADOOP_HOME/sbin/stop-dfs.sh

#
$HADOOP_HOME/sbin/stop-yarn.sh

