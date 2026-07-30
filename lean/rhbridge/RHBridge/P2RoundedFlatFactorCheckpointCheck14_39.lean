import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel14FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel14FlatComponentChunk39

end RHP2Bridge
