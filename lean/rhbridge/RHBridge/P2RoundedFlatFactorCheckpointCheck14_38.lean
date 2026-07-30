import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel14FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel14FlatComponentChunk38

end RHP2Bridge
