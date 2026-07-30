import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel31FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel31FlatComponentChunk42

end RHP2Bridge
