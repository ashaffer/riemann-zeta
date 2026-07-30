import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk7 :
    P2RoundedFactorCheckpointData.panel30Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix28_eq :
    P2RoundedFactorCheckpointData.panel30Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk7.1

theorem panel30Prefix29_eq :
    P2RoundedFactorCheckpointData.panel30Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk7.2.1

theorem panel30Prefix30_eq :
    P2RoundedFactorCheckpointData.panel30Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk7.2.2.1

theorem panel30Prefix31_eq :
    P2RoundedFactorCheckpointData.panel30Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk7.2.2.2

end RHP2Bridge
