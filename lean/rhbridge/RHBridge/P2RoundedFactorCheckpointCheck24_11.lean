import RHBridge.P2RoundedFactorCheckpointData24

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24FactorChunk11 :
    P2RoundedFactorCheckpointData.panel24Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨24, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel24Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨24, by decide⟩ := by
  decide +kernel

theorem panel24Prefix44_eq :
    P2RoundedFactorCheckpointData.panel24Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk11.1

theorem panel24Prefix45_eq :
    P2RoundedFactorCheckpointData.panel24Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk11.2.1

theorem panel24Prefix46_eq :
    P2RoundedFactorCheckpointData.panel24Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk11.2.2.1

theorem panel24Prefix47_eq :
    P2RoundedFactorCheckpointData.panel24Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨24, by decide⟩ := by
  exact panel24FactorChunk11.2.2.2

end RHP2Bridge
