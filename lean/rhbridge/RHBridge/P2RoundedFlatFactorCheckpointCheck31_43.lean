import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel31FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel31FlatComponentChunk43

end RHP2Bridge
