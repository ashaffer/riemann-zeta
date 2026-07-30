import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel14FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel14FlatComponentChunk31

end RHP2Bridge
