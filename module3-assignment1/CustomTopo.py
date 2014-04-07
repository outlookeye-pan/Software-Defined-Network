'''
Coursera:
- Software Defined Networking (SDN) course
-- Module 3 Programming Assignment

Professor: Nick Feamster
Teaching Assistant: Muhammad Shahbaz
'''

from mininet.topo import Topo

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        # Add your logic here ...
        self.fanout = fanout
        #from top to bottom, left to right order, to construct the tree topology
        core = self.addSwitch('c1')
		for i in irange(1,fanout):
            aggregation = self.addSwitch('a%s'%i)
            self.addLink(core, aggregation, **linkopts1)
            for j in irange(1, fanout)
                edge = self.addSwitch('e%s' %((i-1)*fanout+j))
                self.addLink(aggregation, edge, **linkopts2)
                for k in irange(1, fanout)
                    host = self.addHost('h%s' %( ((i-1)*fanout + j - 1)*fanout +k ))
                    self.addLink(edge, host, **linkopts3)
        
                    
#topos = { 'custom': ( lambda: CustomTopo() ) }
def datacenterTest():    
    topos = { 'custom': ( lambda: CustomTopo(fanout = 2) ) }
    net = Mininet(topo)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    print "Testing network connectivity"
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    datacenterTest()
