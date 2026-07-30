import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel31FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel31FlatComponentChunk29

end RHP2Bridge
