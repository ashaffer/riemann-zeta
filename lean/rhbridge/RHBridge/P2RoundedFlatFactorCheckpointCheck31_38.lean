import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel31FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel31FlatComponentChunk38

end RHP2Bridge
