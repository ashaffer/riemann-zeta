import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk9 :
    P2RoundedFactorCheckpointData.panel30Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix36_eq :
    P2RoundedFactorCheckpointData.panel30Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk9.1

theorem panel30Prefix37_eq :
    P2RoundedFactorCheckpointData.panel30Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk9.2.1

theorem panel30Prefix38_eq :
    P2RoundedFactorCheckpointData.panel30Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk9.2.2.1

theorem panel30Prefix39_eq :
    P2RoundedFactorCheckpointData.panel30Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk9.2.2.2

end RHP2Bridge
