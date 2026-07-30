import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk7 :
    P2RoundedFactorCheckpointData.panel15Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix28_eq :
    P2RoundedFactorCheckpointData.panel15Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk7.1

theorem panel15Prefix29_eq :
    P2RoundedFactorCheckpointData.panel15Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk7.2.1

theorem panel15Prefix30_eq :
    P2RoundedFactorCheckpointData.panel15Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk7.2.2.1

theorem panel15Prefix31_eq :
    P2RoundedFactorCheckpointData.panel15Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk7.2.2.2

end RHP2Bridge
