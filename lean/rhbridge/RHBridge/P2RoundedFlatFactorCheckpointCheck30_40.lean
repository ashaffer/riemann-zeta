import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel30FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel30FlatComponentChunk40

end RHP2Bridge
