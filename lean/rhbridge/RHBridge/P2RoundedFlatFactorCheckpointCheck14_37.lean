import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel14FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel14FlatComponentChunk37

end RHP2Bridge
