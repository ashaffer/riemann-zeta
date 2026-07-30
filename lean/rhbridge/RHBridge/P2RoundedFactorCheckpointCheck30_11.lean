import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk11 :
    P2RoundedFactorCheckpointData.panel30Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix44_eq :
    P2RoundedFactorCheckpointData.panel30Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk11.1

theorem panel30Prefix45_eq :
    P2RoundedFactorCheckpointData.panel30Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk11.2.1

theorem panel30Prefix46_eq :
    P2RoundedFactorCheckpointData.panel30Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk11.2.2.1

theorem panel30Prefix47_eq :
    P2RoundedFactorCheckpointData.panel30Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk11.2.2.2

end RHP2Bridge
