import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel14FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel14FlatComponentChunk24

end RHP2Bridge
