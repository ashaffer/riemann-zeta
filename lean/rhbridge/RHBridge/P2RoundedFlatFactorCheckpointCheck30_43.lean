import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel30FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel30FlatComponentChunk43

end RHP2Bridge
