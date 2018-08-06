import p2p_daemon
import p2p_status
import common.test as t

t.RegisterTest(p2p_daemon.Test, "P2P Daemon check")
t.RegisterTest(p2p_status.Test, "P2P Status check")