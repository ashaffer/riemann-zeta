import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk7 :
    P2RoundedFactorCheckpointData.panel12Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix28_eq :
    P2RoundedFactorCheckpointData.panel12Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk7.1

theorem panel12Prefix29_eq :
    P2RoundedFactorCheckpointData.panel12Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk7.2.1

theorem panel12Prefix30_eq :
    P2RoundedFactorCheckpointData.panel12Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk7.2.2.1

theorem panel12Prefix31_eq :
    P2RoundedFactorCheckpointData.panel12Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk7.2.2.2

end RHP2Bridge
