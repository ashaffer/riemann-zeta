import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel14FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel14FlatComponentChunk30

end RHP2Bridge
