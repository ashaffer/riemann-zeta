import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel14FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel14FlatComponentChunk25

end RHP2Bridge
