import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel14FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel14FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel14FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel14TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel14FlatComponentChunk32

end RHP2Bridge
