import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel14FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel14FlatComponentChunk45

end RHP2Bridge
