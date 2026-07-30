import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel14FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel14FlatComponentChunk44

end RHP2Bridge
