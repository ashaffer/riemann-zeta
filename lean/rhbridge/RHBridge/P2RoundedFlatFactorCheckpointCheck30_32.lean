import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk32 :
    P2RoundedFactorCheckpointData.panel30FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd8_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd8 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨8, by decide⟩ := by
  exact panel30FlatComponentChunk32

end RHP2Bridge
