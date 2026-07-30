import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel30FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel30FlatComponentChunk36

end RHP2Bridge
