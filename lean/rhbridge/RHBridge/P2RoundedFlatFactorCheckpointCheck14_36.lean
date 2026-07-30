import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel14FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel14FlatComponentChunk36

end RHP2Bridge
