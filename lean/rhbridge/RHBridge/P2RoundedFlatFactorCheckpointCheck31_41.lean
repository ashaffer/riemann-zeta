import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel31FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel31FlatComponentChunk41

end RHP2Bridge
