import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel14FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel14FlatComponentChunk29

end RHP2Bridge
