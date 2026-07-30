import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel14FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel14FlatComponentChunk27

end RHP2Bridge
