import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel14FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel14FlatComponentChunk34

end RHP2Bridge
