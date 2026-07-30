import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel31FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel31FlatComponentChunk28

end RHP2Bridge
